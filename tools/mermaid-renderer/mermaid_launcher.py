import sys
import os
import subprocess
from mcp.server.fastmcp import FastMCP

import shutil
from pathlib import Path

# 1. MCP 서버 초기화
mcp = FastMCP("Mermaid-Renderer")

# 2. 렌더링을 위한 기본 경로 설정
# 전역 설치된 mmdc 자동 감지
MMDC_PATH = shutil.which("mmdc") or shutil.which("mmdc.cmd")

# 이미지 저장 기본 경로 (크로스플랫폼)
ARTIFACTS_DIR = Path.home() / ".gemini" / "antigravity" / "artifacts" / "mermaid"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

@mcp.tool()
async def render_mermaid(code: str, filename: str, output_format: str = "png") -> str:
    """
    Mermaid 다이어그램 코드를 이미지 파일(PNG 또는 SVG)로 변환합니다.
    
    Args:
        code: Mermaid 다이어그램 소스 코드
        filename: 저장할 파일 이름 (확장자 제외)
        output_format: 'png' 또는 'svg' (기본값: 'png')
    
    Returns:
        생성된 이미지 파일의 절대 경로
    """
    # 임시 mmd 파일 생성
    input_file = str(ARTIFACTS_DIR / f"{filename}.mmd")
    output_file = str(ARTIFACTS_DIR / f"{filename}.{output_format}")
    
    try:
        with open(input_file, "w", encoding="utf-8") as f:
            f.write(code)
        
        # mmdc 명령어 실행
        if MMDC_PATH:
            cmd = [MMDC_PATH, "-i", input_file, "-o", output_file]
        else:
            cmd = [shutil.which("npx") or "npx", "-y", "@mermaid-js/mermaid-cli", "-i", input_file, "-o", output_file]
        
        # 추가 인자 (해상도 등) 설정 가능
        if output_format == "png":
            cmd.extend(["-b", "white", "-p", "puppeteer-config.json"]) # 배경색 흰색, 설정 파일(필요시)

        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # 완료 후 입력 파일 삭제 (옵션)
        if os.path.exists(input_file):
             os.remove(input_file)
             
        return f"성공: {output_file}"
    except subprocess.CalledProcessError as e:
        return f"렌더링 오류: {e.stderr}"
    except Exception as e:
        return f"오류 발생: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
