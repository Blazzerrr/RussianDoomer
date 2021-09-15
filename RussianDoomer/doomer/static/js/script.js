$(document).ready(function(){
    $('div#messages').scrollTop($('div#messages').get(0).scrollHeight);
    $('div#donations').scrollTop(0);

    changeDefaultVolume()

    setInterval(checkNewMessages, 2000);
    setInterval(checkNewDonations, 2000);

    function changeDefaultVolume(){
        var element = document.getElementById("audioPlayeer"); 
        element.volume = 0.5;
    };
    
    function checkNewMessages(){
        $.ajax("messages.json", {
            ifModified: true,
            success: function(messages, status) { 
                if (status == "success") {
                    if (!messages)
                        return;

                    var p = document.getElementById('lastIdMessages');
                    var text = p.textContent;
                    var last_id = Number(text);

                    for(var i = 0; i < messages.length; i++)
                        {
                            var msg = messages[i];
                            if (msg.id > last_id)
                            {
                                document.getElementById("messages").innerHTML += '<div class="message"><span class="sender_message"><p>' + msg.datetime + ' ' + msg.name + '</p></span><span class="text_message"><p>' + msg.message + '</p></span></div>';
                                $('div.messages').data('lastIdMessages', msg.id);
                                $('div#messages').scrollTop($('div#messages').get(0).scrollHeight);  
                            }
                        }
                }
        }
    });
    };

    function checkNewDonations(){
        $.ajax("donations.json", {
            ifModified: true,
            success: function(donations, status) { 
                if (status == "success") {
                    if (!donations)
                        return;

                    var p = document.getElementById('lastIdDonations');
                    var text = p.textContent;
                    var last_id = Number(text);

                    for(var i = 0; i < donations.length; i++)
                        {
                            var d = donations[i];
                            if (d.donateId > last_id)
                            {
                                var appendingData = '<div class="donation"><span class="donate_name"><h1>' + ' ' + d.username + ' ' + '- ' + d.amount + ' ' + d.currency + '</h1></span><span class="donate_message"><p>' + ' ' + d.message + '</p></span></div>';
                                document.getElementById("donations").innerHTML = appendingData + document.getElementById("donations").innerHTML
                                $('div.donations').data('lastIdDonations', d.donateId);
                                $('div#donations').scrollTop(0); 
                            }
                        }
                }
        }
    });
    };

    $(document).on( 'click', '#submit', function() {
        var name = $("#name").val();
        var message = $("#message").val();

        if(message.length > 300 || name.length > 32)
        {
            alert("Максимальная длина сообщения: 300 символов\nМаксимальная длина имени: 32 символа");
            return false;
        }
        if (name == '' || message == '')
        {
            alert("Поле сообщения или имени не может быть пустым")
            return false;
        }

        $.ajax(
        {
            url: 'sendMessage',
            type: 'post',
            data: {
                name: name,
                message: message,
            },

            success: function(output)
            {
                $('#name').val('');
                $('#message').val('');
                checkNewMessages();
            }
        });
    });
});


function Random()
{
	$.ajax(
	{
		url: 'https://russiandoomer.ru/randomMusic',
		type: 'get',
		contentType: 'application/json',
		success: function(output)
		{
            output = JSON.stringify(output);
            var name = JSON.parse(output).name;
            var path = JSON.parse(output).path;
            var element = document.getElementById("audioPlayeer"); 
            element.src = path;

            name = name.replace(/_/g, ' ')
            name = name.replace(/.mp3/g, '')

            document.getElementById("nameMusic").innerHTML = name;
            document.getElementById("all_history").innerHTML += '<li class = "tracks_history" onclick = Play("' + path + '")>' + name + '</li>';
		}
	});
}


function Play(path) {
    splitPath = path.split('/');
    var name = splitPath[splitPath.length - 1].replace(/_/g, ' ');
    var element = document.getElementById("audioPlayeer"); 
    element.src = path;
    document.getElementById("nameMusic").innerHTML = name;
}
