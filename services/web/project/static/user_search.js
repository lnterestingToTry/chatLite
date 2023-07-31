const input_user_search = document.getElementById("user_nickname")

function onChange() {
    const input_value = input_user_search.value;

    if (input_value !== ""){

        fetch('/user_bynickname_search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({input_value})
        })
        .then((response) => response.json())
        .then((data) => {
            const user_search = document.getElementById("user_search")

            user_search.innerHTML = ""

            users = users_list(data, user_search)

            console.log(data);
        })
        .catch((error) => { 
            console.log(error);
        });
    }
}

input_user_search.addEventListener('input', onChange)