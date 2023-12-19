export const prerender = true;

import { token } from '$lib/stores/userStore.js';
import { get } from 'svelte/store';

export async function load({ params }) {
    let response = await fetch("http://localhost:8000/api/v1/relatives/", {
        headers: {
            Authorization: `Token ${get(token)}`
        }
    });
    let relatives = await response.json();
    return {
        relatives: relatives
    };
}