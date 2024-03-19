# HR-ADUC-Datasimulator

HR-ADUC-Datasimulator는 Active Directory 사용자 및 그룹 속성에 대한 시뮬레이션 데이터를 생성하기 위한 Python 스크립트입니다. 실제 사용자 정보 대신 시뮬레이션 데이터를 사용하여 데이터 추출 프로세스의 테스트 및 데모를 용이하게하는 것을 목표로합니다.

## 전제 조건

이 스크립트를 올바르게 작동하려면 다음 전제 조건이 충족되어야합니다.
1. 스크립트를 실행하는 기기에 Python이 설치되어 있어야합니다. 이 스크립트의 개발에 사용된 버전은 3.12.2입니다. 3.6 이상의 버전을 사용하는 것이 좋습니다.
2. 다음 모듈이 설치되어 있어야합니다.
    a. pandas:
        이 라이브러리는 데이터 구조 및 데이터 분석 도구를 제공합니다.
    b. configparser:
        이 모듈은 INI 형식의 설정 파일로 작업할 수 있도록합니다.
    c. Faker:
        이 라이브러리는 이름, 주소, 전화 번호 등의 가짜 데이터를 생성합니다.
    d. random 또는 random2:
        이러한 모듈은 임의의 숫자를 생성하기 위한 함수를 제공합니다.
    e. math:
        이 모듈은 삼각 함수, 지수 함수, 로그 함수 등의 표준 수학 함수 집합을 제공합니다.
    f. unidecode:
        이 모듈은 Unidecode 문자열을 ASCII로 변환합니다.

configparser, random 및 math 모듈은 일반적으로 Python에 포함되어 있습니다.
pandas, Faker 및 unidecode 모듈은 외부 패키지입니다.

## 특징

- Active Directory (AD) 계정의 속성을 추출하기 위한 무작위 데이터를 생성합니다.
- 실제 사용자 정보를 노출하지 않고 데이터 추출 프로세스를 데모합니다.
- AD 계정과 인사 (HR) 추출 간의 데이터 일관성을 테스트하고 확인할 수 있습니다.
- ADUC 서버의 보안을 향상시키기 위해 이상을 강조하고 수정 제안을 제공합니다.

## 사용법

1. 리포지토리를 로컬 컴퓨터로 클론하거나 다운로드합니다.
2. 귀하의 언어에 해당하는 parameters_[XX].ini 파일을 복제하고, parameters.ini로 이름을 변경하십시오.
3. parameters.ini 파일을 사용하여 데이터 생성 프로세스에 대한 특정 설정을 정의합니다.
4. HR-ADUC-Datasimulator.py 스크립트를 실행하여 시뮬레이션 데이터를 생성합니다.
5. 출력을 분석하여 테스트, 데모 또는 보안 개선 목적으로 사용합니다.

## 라이선스

HR-ADUC-Datasimulator는 GNU Lesser General Public License v3.0 (LGPL-3.0)에 따라 라이선스가 부여됩니다. 이 라이선스의 조건에 따라이 스크립트를 사용, 수정 및 배포할 수 있습니다.

자세한 내용은 [LICENSE](https://github.com/ShaoLunix/HR-ADUC-Datasimulator/blob/main/LICENSE) 파일을 참조하십시오.

## 기여

이 프로젝트에 기여는 환영입니다. 문제가 발생하거나 개선 제안이 있거나 새로운 기능을 기여하려면 GitHub에서 문제를 열거나 풀 요청을 제출하십시오.

## 면책 조항

이 스크립트는 어떠한 종류의 보증도없이 "있는 그대로"제공됩니다. 자체 책임하에 사용하십시오.

## 저자

Stéphane-Hervé

## 연락처

질문, 피드백 또는 지원이 필요한 경우 https://github.com/ShaoLunix/HR-ADUC-Datasimulator/issues 로 연락하십시오.
