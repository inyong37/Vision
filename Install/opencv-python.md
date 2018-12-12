1. Anaconda 설치 (프로그래밍 언어 python과 다양한 library가 포함된 패키지)
python3 버전 중 자신의 랩탑 환경에 맞게 설치 (Windows/OS X/Ubuntu 등)
https://www.anaconda.com/download/

1-1. 설치 중
진행하다가 선택하는 거에서 All Users 선택
더 진행하다가 선택하는 거에서 Add anaconda to the system PATH environment variable도 같이 선택

2. Pycharm 설치 (C언어의 Visual Studio 같은 Python 실행하는 툴 중 한가지)
자신의 랩탑 환경에 맞게 설치 (professional 버전은 1달 무료지만 학교 이메일로 등록하면 1년 라이센스로 사용 가능(그리고 카톡 친구에 사용 인증하면 스타벅스 줌/community 버전은 쭉 무료)
https://www.jetbrains.com/pycharm/download/#section=windows

3. 윈도우 검색에서 anaconda prompt를 찾은 뒤 오른쪽 마우스 클릭으로 관리자 권한으로 실행
아래 명령어 입력 (python 패키지 관리툴 설치)
conda install -c anaconda pip
그리고 아래 명령어 입력 (opencv 중 python꺼를 다운로드 및 설치)
pip install opencv-python

4. 이제 pycharm을 실행하면 처음에 폴더/프로젝트를 만들고 화면이 뜨는데 python과 아나콘다로 설치된 library들을 불러오느라 시간이 좀 걸림
python 언어는 c언어의 컴파일러와 달리 interpreter가 조금 다르지만 비슷한 역할을 하는데 만약 interpreter가 없다고 알림이 뜨면
anaconda prompt를 실행하고 conda info --envs 명령어를 치면 환경과 경로가 나오는데 그 경로를 기억하고
pycharm에서 setting에서 interpreter 설정에 들어가서 기억한 경로로 들어가서 (Anaconda3 폴더 내) python.exe를 선택하면 됨

5. 나머지는 python script를 하나 만들어서 이제 코딩하면 됨
