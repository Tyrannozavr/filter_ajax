$('#price').on('click', function(){ //При клике по элементу с id=price выполнять...
        let url = this.action;
        let params = new URLSearchParams(new FormData(this)).toString();
        $.ajax({
            url: 'ajax/', //Путь к файлу, который нужно подгрузить
            type: 'GET',
            data: params,
            beforeSend: function(){
                $('#content').empty(); //Перед выполнением очищает содержимое блока с id=content
            },
            success: function(responce){
                    $('#content').append(responce); //Подгрузка внутрь блока с id=content
            },
            error: function(){
                alert('Error!');
            }
        });
    });

