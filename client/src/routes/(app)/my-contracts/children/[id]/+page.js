import { token } from '$lib/stores/userStore.js';
import { get } from 'svelte/store';

export async function load({ params }) {
    let response = await fetch(`http://localhost:8000/api/v1/weddings/child/${params.id}/`, {
        headers: {
            Authorization: `Token ${get(token)}`
        }
    });
    let child = await response.json();
    console.log(child);

    return {
        child: child,
        slug: params.id
    };
}