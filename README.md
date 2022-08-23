# 👟 MyLittleShoes

나만의 신발 스타일 만들기

<br />

# 📃 프로젝트 정보

### 1. 제작기간

> 2022.06.28 ~ 07.06

### 2. 참여 인원

> |                    Name                    |  Position   |
> | :----------------------------------------: | :---------: |
> | [김동우](https://github.com/kimphysicsman) |    Back     |
> |   [김진수](https://github.com/creamone)    |    Back     |
> |     [박진우](https://github.com/J1NU2)     |    Back     |
> |    [최민기](https://github.com/mankic)     |    Back     |

### 3. 역할 분담

> - 김동우 : 회원가입 / 로그인 기능 / Generative model 사용
> - 김진수 : 추천 스타일 페이지
> - 박진우 : 이미지 업로드 + 결과 페이지 (결과 페이지에서 저장을 누르면 히스토리에 저장됨)
> - 최민기 : 히스토리(게시판) 페이지 / 좋아요 / 댓글 / 즐겨찾기 기능

<br />

# 📚 기술 스택

### 1. Back-end

> python3  
> Django  
> Django-rest-framwork

### 2. Front-end

> Node.js

<br />

# 📊 ERD

<details>
<summary>ERD</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a1b9badd-e923-4a82-abc8-6a72480a1f77/mylittleshoes_%281%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220823T071050Z&X-Amz-Expires=86400&X-Amz-Signature=7023202f6ba7b54d834bb0d2cca9a9dfd7ce20d41727db6a98a07a62a8d4bfdc&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22mylittleshoes%2520%281%29.png%22&x-id=GetObject" width="800px"/>
</div>
</details>

<br />

# 🔑 핵심기능

### 1. 회원가입 / 로그인 기능

> 사용자가 사이트에서 회원가입을 하여 DB에 저장하고  
> DB에 해당 사용자 정보가 있으면 로그인이 가능하도록 합니다.  
> [코드 보러가기](https://github.com/nbcamp-AI-2-fantastic4/mylittleshoes_backend/blob/c13591158515c0ece14190d953593131e7b4a071/user/views.py#L12)

### 2. 이미지 업로드 + 결과 이미지 생성

> 사용자가 이미지를 업로드하여 새로운 결과 이미지를 생성하고  
> 저장하기 버튼을 누르면 DB에 이미지들이 저장됩니다.  
> [코드 보러가기](https://github.com/nbcamp-AI-2-fantastic4/mylittleshoes_backend/blob/c13591158515c0ece14190d953593131e7b4a071/upload/views.py#L36)

### 3. 추천 스타일 페이지

> 다양한 스타일을 추천해주는 페이지를 보여줍니다.  
> [코드 보러가기](https://github.com/nbcamp-AI-2-fantastic4/mylittleshoes_backend/blob/c13591158515c0ece14190d953593131e7b4a071/recommend/views.py#L12)

### 4. 게시판 페이지 (히스토리 + 좋아요 + 댓글 기능)

> 저장된 이미지들을 불러와서 하나의 게시글을 생성하고  
> 해당 게시글에서 댓글 및 좋아요를 남길 수 있도록 합니다.  
> [코드 보러가기](https://github.com/nbcamp-AI-2-fantastic4/mylittleshoes_backend/blob/c13591158515c0ece14190d953593131e7b4a071/history/views.py#L16)

<br />

# 📕 기타 자료

### 1. 기획문서

> [MyLittleShoes - Notion](https://www.notion.so/kimphysicsman/MLS-My-Little-Shoes-2d7eafdb6a514ae7a569f11cc04411e1)

### 2. Generative model

> [style-transfer-pytorch - Github](https://github.com/crowsonkb/style-transfer-pytorch)

### 3. 발표영상

<table>
  <tbody>
    <tr>
      <td>
        <p align="center"> 22.07.06 발표 </p>
        <a href="https://www.youtube.com/watch?v=-UBy-KnmZs4" title="MyLittleShoes 발표">
          <img align="center" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d3d05756-264f-4f13-bf98-8d823f012d02/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220823T073555Z&X-Amz-Expires=86400&X-Amz-Signature=ca1ce99ba02ee89c5986be87c819a9bb4f1d218329b5ee3da6dc81a6bfe7d1cf&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject" width="300" >
        </a>
      </td>
    </tr>
  </tbody>
</table>
