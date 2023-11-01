## 🎬 영화 추천 사이트 Moolog

<p align="center"><img src="./image/logo.png"/></p>

    📌SSAFY 9기 1학기 관통프로젝트
    📌23.05.17 ~ 23.05.26

### 📑 목차

1. 서비스 소개
2. 기술 스택
3. 아키텍처
4. ERD
5. 기능 살펴보기
6. 팀원 소개 및 역할

### 🔍 서비스 소개
---
> 사용자 취향 기반 영화 추천 및 영화 특화 SNS 프로젝트 입니다.

많은 OTT 서비스들이 출시되어있는 현재 사람들은 무엇을 볼 지에 대해서 고민하는 시간이 점점 길어지고 있습니다. 너무 많은 선택권이 주어지다보니 오히려 선택이 힘들어지는 상황에 놓이게 되었습니다.이러한 사용자들의 고민을 덜어주고자 해당 프로젝트를 기획하게 되었습니다.<br>
사용자가 좋아요를 누른 영화를 기반으로 장르를 분석하여 추천 알고리즘을 통해 10개의 영화를 추천해줍니다. 또한 본인이 좋아하는 사용자를 팔로우하여 사용자 간의 영화에 대한 인사이트를 나눌 수 있는 영화 특화 SNS 기능 또한 제공합니다.


### 🔍 기술 스택
---

<table>
<tr>
 <td align="center">언어</td>
 <td>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=ffffff"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>
    
    
 </td>
</tr>
<tr>
 <td align="center">프레임워크</td>
 <td>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=ffffff"/>
    <img src="https://img.shields.io/badge/Vue-41B883?style=for-the-badge&logo=vue.js&logoColor=ffffff"/>  
</tr>
<tr>
 <td align="center">라이브러리</td>
 <td>
<img src="https://img.shields.io/badge/vuetify-1867C0?style=for-the-badge&logo=Vuetify&logoColor=ffffff"/>
<img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=ffffff"/>
<img src="https://img.shields.io/badge/vue router-41B883?style=for-the-badge&logo=&logoColor=ffffff"/>
<img src="https://img.shields.io/badge/lodash-3492FF?style=for-the-badge&logo=lodash&logoColor=ffffff"/>
<img src="https://img.shields.io/badge/axios-5A29E4?style=for-the-badge&logo=axios&logoColor=ffffff"/>
<img src="https://img.shields.io/badge/django allauth-000000?style=for-the-badge&logo=django-allauth&logoColor=ffffff"/>

</tr>
<tr>
 <td align="center">패키지 매니저</td>
 <td>
    <img src="https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white">
  </td>
</tr>
<tr>
 <td align="center">인프라</td>
 <td>
  <img src="https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=SQlite&logoColor=ffffff"/>  
</tr>
<tr>
 <td align="center">포맷팅</td>
 <td>
  <img src="https://img.shields.io/badge/ESLint-4B32C3?style=for-the-badge&logo=ESLint&logoColor=ffffff"/> 
  <img src="https://img.shields.io/badge/Prettier-F7B93E?style=for-the-badge&logo=Prettier&logoColor=ffffff"/> 
  </td>
</tr>

<tr>
 <td align="center">협업툴</td>
 <td>
    <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"/> 
    <img src="https://img.shields.io/badge/Gitlab-FC6D26?style=for-the-badge&logo=Gitlab&logoColor=white"/> 
    <img src="https://img.shields.io/badge/Mattermost-0058CC?style=for-the-badge&logo=Mattermost&logoColor=white"/> 
 </td>
</tr>
<tr>
 <td align="center">기타</td>
 <td>
    <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=Figma&logoColor=white"/>
    <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white"/> 
    <img src="https://img.shields.io/badge/swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=white"/>
    <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>
 </td>
</tr>
</table>


### 🔍 기능 살펴보기
---
#### 🎥 로그인
![로그인](./image/로그인.gif)

#### 🎥 회원가입
![회원가입](./image/회원가입.gif)

#### 🎥 비밀번호 찾기
![비밀번호 찾기](./image/비밀번호%20찾기.gif)

#### 메인화면(로그인X)
![메인화면(로그인x)](./image/메인화면(로그인X).gif)

#### 🎥 메인화면(로그인O)
![메인화면(로그인O)](./image/메인화면(로그인O).gif)

#### 🎥 추천 영화(좋아요 누르기 전후) & 영화 검색
![추천 영화(좋아요 누르기 전후) & 영화 검색](./image/영화%20좋아요%20전후%20및%20영화%20검색.gif)

#### 🎥 영화목록 호버
![영화목록 호버](./image/영화목록%20호버.gif)

#### 🎥 영화 상세페이지
![영화 상세페이지](./image/영화%20상세페이지.gif)

#### 🎥 마이프로필
![마이프로필](./image/마이%20페이지(프로필%20이미지,%20닉네임%20변경).gif)

#### 🎥 게임 1 : 슬라이드 퍼즐게임
![게임 1](./image/슬라이드%20퍼즐%20게임.gif)

#### 🎥 게임 2 : 같은 그림 찾기
![게임 2](./image/같은%20그림%20찾기.gif)

### 🧚‍♀️팀원 소개 및 역할
| 이름   | 기능 및 역할 |
| ----|--------------------------------------------------------------------------- |
| 이연지 |  팀장, BackEnd(회원가입, 로그인, 비밀번호 찾기(이메일 인증), 외부 API 통신, 더미데이터 형성, 영화 조회, 영화 추천 알고리즘, 영화 검색 기능)</br>FrontEnd(메인페이지 - 로그인 유무에 따른 분기 처리, 영화 목록, 영화 검색, 이스터 에그, 게임 페이지 CSS, 유저 정보 페이지)|
| 조혜진 |  팀원, FrontEnd </br> REST API 적용 로그인, 회원가입, 팔로잉 및 영화 좋아요 기능, 유튜브 API 영화 예고편, 영화 상세페이지, 게임 기능 구현 |
