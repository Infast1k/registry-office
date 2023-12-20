import { token } from '$lib/stores/userStore.js';
import { get } from 'svelte/store';

export async function load({ params }) {
    let response = await fetch(`http://localhost:8000/api/v1/admin/users/${params.id}/`, {
        headers: {
            Authorization: `Token ${get(token)}`
        }
    });
    let user = await response.json();

    return {
        user: user,
        slug: params.id
    };
}