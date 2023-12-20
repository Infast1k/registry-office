import { token } from '$lib/stores/userStore.js';
import { get } from 'svelte/store';

export async function load({ params }) {
    let wedding_response = await fetch(`http://localhost:8000/api/v1/weddings/${params.id}/`, {
        headers: {
            Authorization: `Token ${get(token)}`
        }
    });
    let contract = await wedding_response.json();


    let witnesses_response = await fetch(`http://localhost:8000/api/v1/weddings/witnesses/${params.id}/`, {
        headers: {
            Authorization: `Token ${get(token)}`
        }
    });
    let witnesses = await witnesses_response.json();

    return {
        contract: contract,
        witnesses: witnesses,
        slug: params.id
    };
}