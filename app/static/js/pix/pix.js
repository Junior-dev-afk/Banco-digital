async function loadPage () {
    await global.verifySession()

    clearInputs();
}

window.addEventListener("load", async () => {
    await loadPage()
})