import { token } from '$lib/stores/userStore.js';
import { get } from 'svelte/store';

export async function load({ params }) {
    let response = await fetch(`http://localhost:8000/api/v1/relatives/${params.id}/`, {
        headers: {
            Authorization: `Token ${get(token)}`
        }
    });
    let relative = await response.json();

    return {
        relative: {
            last_name: relative.last_name,
            phone: relative.phone,
            address: relative.address
        },
        slug: params.id
    };
}