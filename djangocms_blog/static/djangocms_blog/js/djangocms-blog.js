function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

  //Custom notify for blog post
  $(".post-item").on('click',function(){
    let postid=$(this).attr('data-postid');
    $(`.notify-reply[data-postid="${postid}"]`)[0].innerHTML='';
    $.ajax({
      method:'POST',
      url:'notify/',
      data:{
        csrfmiddlewaretoken:getCookie('csrftoken'),
        postid:postid
      }

    }).
    done(function(data){
      css=`.notify-reply[data-postid="${data.postid}"]`;
      $(css)[0].innerHTML=data.message;
    }).
    fail(function(data){
      //css=`+ .notify-reply[data-postid="${data.postid}"]`;
      $('+ .notify-reply')[0].innerHTML='Notification Failed';
    });
  })