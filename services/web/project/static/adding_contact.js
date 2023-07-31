function adding_contact(user_id){
    fetch('/adding_contact',
    {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({user_id}), //contact id to add
    })
    .then((response) => {
        get_users()
    });
}