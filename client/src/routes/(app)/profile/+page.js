import { token, role } from '$lib/stores/userStore.js';
import { get } from 'svelte/store';
import { goto } from '$app/navigation';

export async function load({ params }) {
    let response = await fetch(`http://localhost:8000/api/v1/profile/`, {
        headers: {
            Authorization: `Token ${get(token)}`
        }
    });
    let user = await response.json();
    role.set(user.role.role_name)
    if (!user.profile) {
        goto("/profile/create-profile")
        return;
    }
    return {
        user: user
    };
}