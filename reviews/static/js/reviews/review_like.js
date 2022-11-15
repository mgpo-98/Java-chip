const likeBtn = document.querySelector('.like-forms')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

// (2) 좋아요 버튼을 클릭하면, 함수 실행
forms.forEach((form) => {

    form.addEventListener('click', function (event) {
        // 서버로 비동기 요청(axios)을 하고 싶음
        event.preventDefault()
        console.log(event.currentTarget.dataset.reviewId)
        axios({
            method: 'post',
            url: `/reviews/${event.target.dataset.reviewId}/like/`,
            headers: { 'X-CSRFToken': csrftoken },
        })
            .then((response) => {
                console.log(response)
                console.log(response.data)
                const isLiked = response.data.is_liked
                const likeBtb = document.querySelector(`#like-${reviewId}`)
                likeReview.classList.toggle('bi-heart-fill')
                // 다음 주석 처리한 내용과 동일

                if (isLiked === true) {
                    likeBtn.value = '좋아요 취소'
                } else {
                    likeBtn.value = '좋아요 '
                }

            })
    })
})