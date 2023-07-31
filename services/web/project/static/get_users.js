function get_users(){
    fetch('/get_users',
    {
        method: 'GET',
    })
    .then((response) => response.json())
    .then((data) => {
        const contacts = document.getElementById("contacts")

        contacts.innerHTML = ""

        users = users_list(data, contacts)
        
        console.log(data);
    })
    .catch((error) => { 
        console.log(error);
    });
}