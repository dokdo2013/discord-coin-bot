# 세주코인봇
- 디스코드에서 사용 가능한 코인 시세, 차트 검색 봇입니다.
- [봇 링크](https://discord.com/oauth2/authorize?client_id=819819757246087218&scope=bot)

## 코인 명령어
- $도움말 : 도움말 정보 받기
- $업비트 {코인명} : 업비트 현재 시세 받기 (예시 : $업비트 비트코인)
- $일봉 {코인명} : 업비트 차트 검색 (예시 : $일봉 비트코인)
- $주봉 {코인명} : 업비트 차트 검색 (예시 : $주봉 비트코인)
- $월봉 {코인명} : 업비트 차트 검색 (예시 : $월봉 비트코인)
- $분봉 {코인명} {검색주기} : 업비트 차트 검색 (예시 : $분봉 비트코인 1) (분봉은 1,3,5,10,30,60,240 초 단위만 지원합니다.)
- $한강 : 현재 한강수온 검색
- $버전 : 현재 버전 정보 조회

## 이용 유의사항
- 현재는 업비트 시세만 검색 가능합니다. 차후 국내, 해외 거래소 정보들도 업데이트할 예정입니다.
- 차트는 데이터를 받아와 직접 그리는 방식으로 서버 상황에 따라 전송이 지연될 수 있습니다.
- 한강 수온 데이터는 서울특별시 OpenAPI를 통해 실시간으로 받아오는 것으로, 서울특별시 API 서버 상태에 따라 전송이 원활하지 않을 수 있습니다.

## 버전 정보
[현재] v 0.1.5 : 분봉, 주봉, 월봉 기능 추가

- v 0.1.4 : 일봉 기능 추가
- v 0.1.3 : 한강 수온 API 엔드포인트 변경 (외부 API -> 서울특별시 OpenAPI)
- v 0.1.2 : 한강 수온 검색 기능 추가
- v 0.1.1 : 업비트 시세정보 검색 기능 개선
- v 0.1.0 : 첫 버전 릴리즈

## License
GNU GPL 3.0
