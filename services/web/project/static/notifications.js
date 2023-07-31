function is_notification(){
    fetch('/is_notification',
    {
        method: 'GET',
    })
    .then((response) => response.json())
    .then((data) => {
        const notifications = document.getElementById("notifications")
        
        if (data[0]['is_notification'] == 'false'){
            notifications.innerHTML = "нуль повідомлень"
        }
        else{
            notifications.innerHTML = "не нуль повідомлень"
        }

        console.log(data);
    });
}

setInterval(is_notification, 3000); //3000 - 3 seconds