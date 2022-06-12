function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Настройка AJAX
$(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});

function to_bookmarks()
{
    var current = $(this);
    var type = current.data('type');
    var pk = current.data('id');
    var action = current.data('action');

    $.ajax({
        url : "/base/" + pk + "/" + action + "/",
        type : 'POST',
        data : { 'pk' : pk },

        success : function (json) {
          $('.bookmark').each((index, el) => {
              const id = $(el).data('id')

              if (id == json.id && $(el).hasClass('added')) {
                  $(el).removeClass('added')
              }
              else if (id == json.id ){
                  $(el).addClass('added')
              }
          })
        }
    });

    return false;
}

// Подключение обработчика
$(function() {
    $('[data-action="bookmark"]').click(to_bookmarks);
});
