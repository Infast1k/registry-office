import { token } from '$lib/stores/userStore.js';
import { get } from 'svelte/store';

export async function load({ params }) {
    return {
        slug: params.id
    };
}