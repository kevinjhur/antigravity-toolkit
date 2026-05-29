const vscode = require('vscode');
const fs = require('fs');
const path = require('path');
const os = require('os');

/**
 * Agent Auto Linker v2.0 - "Do No Harm" Policy
 */
function activate(context) {
    console.log('Agent Auto Linker v2.0 활성화 완료');

    const config = vscode.workspace.getConfiguration('agentAutoLinker');
    const masterPathRaw = config.get('masterAgentPath');
    const enableAutoLink = config.get('enableAutoLink');
    const enableGitignoreUpdate = config.get('enableGitignoreUpdate');

    if (!masterPathRaw || masterPathRaw.trim() === '') return;

    // 경로 정규화 (절대 경로 보장 및 대소문자 문제 방지 위해 resolve 사용)
    const masterPath = path.resolve(masterPathRaw);

    if (!fs.existsSync(masterPath)) {
        console.warn(`[AgentAutoLinker] 마스터 경로를 찾을 수 없습니다: ${masterPath}`);
        return;
    }

    const workspaceFolders = vscode.workspace.workspaceFolders;
    if (!workspaceFolders) return;

    for (const folder of workspaceFolders) {
        const rootPath = folder.uri.fsPath;
        const agentPath = path.join(rootPath, '.agent');
        const resolvedAgentPath = path.resolve(agentPath);

        // [원칙 1] 현재 워크스페이스가 마스터 폴더 영역이라면 절대 아무것도 안 함 (하극상 방지)
        if (resolvedAgentPath.toLowerCase() === masterPath.toLowerCase() || 
            masterPath.toLowerCase().startsWith(resolvedAgentPath.toLowerCase() + path.sep)) {
            console.log(`[AgentAutoLinker] 마스터 본체 리포지토리 감지. 작동을 중단합니다: ${rootPath}`);
            continue;
        }

        try {
            // [원칙 2] 워크스페이스에 이미 무언가(폴더, 파일, 링크) 존재하면 무조건 건드리지 않음
            const alreadyExists = fs.existsSync(agentPath) || (fs.lstatSync(agentPath, { throwIfNoEntry: false })?.isSymbolicLink());

            if (!alreadyExists && enableAutoLink) {
                createLink(masterPath, agentPath);
            } else if (alreadyExists) {
                console.log(`[AgentAutoLinker] 이미 .agent가 존재하므로 넘어갑니다: ${rootPath}`);
            }

            // [원칙 3] 지능형 .gitignore 관리
            if (enableGitignoreUpdate) {
                updateGitignore(rootPath);
            }
            
        } catch (error) {
            console.error('[AgentAutoLinker] Error:', error);
        }
    }
}

/**
 * 심볼릭 링크(Junction) 생성
 */
function createLink(target, linkPath) {
    try {
        const type = os.platform() === 'win32' ? 'junction' : 'dir';
        fs.symlinkSync(target, linkPath, type);
        vscode.window.showInformationMessage('🚀 Agent Auto Linker: 뇌(.agent) 이식 완료!');
    } catch (e) {
        console.error('[AgentAutoLinker] Link creation failed:', e);
    }
}

/**
 * 지능형 .gitignore 처리 (중복 확인)
 */
function updateGitignore(rootPath) {
    const gitignorePath = path.join(rootPath, '.gitignore');
    const ignoreRule = '.agent';

    try {
        if (!fs.existsSync(gitignorePath)) {
            fs.writeFileSync(gitignorePath, ignoreRule + os.EOL, 'utf8');
            return;
        }

        const content = fs.readFileSync(gitignorePath, 'utf8');
        const lines = content.split(/\r?\n/).map(l => l.trim());

        // 이미 어떤 형태로든 .agent가 등록되어 있는지 확인
        const isAlreadyIgnored = lines.some(line => {
            // 주석 제외
            if (line.startsWith('#')) return false;
            // .agent, .agent/, **/.agent, /.agent 등 패턴 체크를 위해 정규화
            const cleaned = line.replace(/^(\*\*\/|\/)/, '').replace(/\/$/, '');
            return cleaned === '.agent';
        });

        if (!isAlreadyIgnored) {
            let newContent = content;
            if (content.length > 0 && !content.endsWith('\n')) {
                newContent += os.EOL;
            }
            newContent += ignoreRule + os.EOL;
            fs.writeFileSync(gitignorePath, newContent, 'utf8');
            console.log('[AgentAutoLinker] .gitignore에 .agent 추가 완료');
        }
    } catch (e) {
        console.error('[AgentAutoLinker] Gitignore update failed:', e);
    }
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
}
