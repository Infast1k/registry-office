import { writable } from 'svelte/store'

export function createUserStore() {
    const user = writable({
        email,
        token,
    })

    function setEmail(email) {
        user.update((u) => u.email = email)
    }

    function setToken(token) {
        user.update((u) => u.token = token)
    }

    return {
        user,
        setEmail,
        setToken
    }
}