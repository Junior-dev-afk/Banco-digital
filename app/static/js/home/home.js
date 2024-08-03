async function getInfos () {

    let user = await global.getSession()

    let response = await fetch("/getUserInfos", {
        method : "POST",
        headers : {
            "Content-Type" : "application/json"
        },
        body : JSON.stringify({user : user})
    })

    if ( !response.ok ) {
        throw new Error("Erro ao capturar informacoes usuario")
    }

    let data = await response.json()

    return data.response
}


async function loadInfos(){
    let user = await getInfos() 

    let foto = document.querySelector(".foto")
    let ola = document.querySelector(".nome")
    let saldo = document.getElementById("saldo")

    global.saldo = user.saldo

    foto.src = `../../${user.foto}`
    ola.innerHTML = `Olá, ${user.user}`
    saldo.innerHTML = formatCurrency(user.saldo)
}

window.addEventListener('load', async function() {
    await global.verifySession()
    loadInfos()
});

function envPix () {
    window.location.href = `${window.location.origin}/pix`
}

