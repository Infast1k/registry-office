export const prerender = true;


export async function load({ params }) {
    return {
        slug: params.id
    };
}