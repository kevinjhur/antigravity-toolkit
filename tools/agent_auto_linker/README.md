# Agent Auto Linker v2.0 (Smart & Safe)

프로젝트마다 공유되는 마스터 `.agent` 폴더를 자동으로 연결해주는 VS Code 익스텐션입니다.

## 🚀 2.0 주요 변경 사항 (Do No Harm)
- **본체 리포지토리 보호**: 마스터 폴더와 동일하거나 상위 경로인 워크스페이스에서는 절대 동작하지 않습니다.
- **기존 자산 존중**: 워크스페이스에 이미 `.agent`가 (폴더, 파일, 링크 중 하나라도) 존재하면 절대로 건드리지 않습니다.
- **스마트 Gitignore**: 이미 무시 규칙이 등록되어 있다면 중복해서 추가하지 않습니다.

## ⚙️ 설정 방법
1. VS Code 설정에서 `agentAutoLinker.masterAgentPath`를 찾아 마스터 `.agent` 폴더의 절대 경로를 입력합니다.
   - 예: `C:\Users\kevin\.gemini\antigravity-multi-agents\.agent`
2. 새로운 프로젝트 폴더를 열면 수초 내에 자동으로 심볼릭 링크(Junction)가 생성됩니다.

## 🛠️ 기능
- **Auto Link**: `.agent`가 없는 곳에 마스터 링크 생성.
- **Auto Gitignore**: 링크 생성 시 Git 관리 대상에서 자동 제외.
- **Windows Junction**: 관리자 권한 없이도 부드럽게 작동.
