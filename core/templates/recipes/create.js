const LoginSubmit = async (event) => {
    event.preventDefault();
    const FD = new FormData();
    const email = event.target.querySelector("input#email").value;
    const password = event.target.querySelector("input#password").value;
    const response = await fetch("//localhost:3001/api/v1/login", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            password: password,
        }),
    });
    if (parseInt(response.status) === 200) {
        const token = (await response.json()).token;
        localStorage.setItem("token", token);
        window.location.href = "/guests";
        alert(" Login Successful!");
    } else {
        alert("Invalid email or password");
    }


const postData = async (data) => {

        try {
            const response = await fetch("/recipes/create/", {
                method: 'POST',
                body: JSON.stringify(data),
                headers: { 'Content-Type': 'application/json' }
            });
            const responeData = await response.json();
            if (responeData.error) {
                addPopUp(success = false);
            }
            else {
                addPopUp(success = true);
                location.replace('recipes/list/')
    
            }
    
        } catch (err) {
            console.log(err);
        }
    
    
};

const form = document.querySelector("form#form").addEventListener('submit', (event) => {

        event.preventDefault();
        const FD = new FormData();
        
        const brand = event.target.querySelector("#brand").value;
        const model = event.target.querySelector("#model").value;
    
        postData({ "brand": brand, "model": model });
    
    
});