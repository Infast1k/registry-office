export const prerender = true;

import { token } from '$lib/stores/userStore.js';
import { get } from 'svelte/store';

export async function load({ params }) {
    let response = await fetch("http://localhost:8000/api/v1/employee/weddings/", {
        headers: {
            Authorization: `Token ${get(token)}`
        }
    });
    let contracts = await response.json();
    return {
        contracts: contracts
    };
}