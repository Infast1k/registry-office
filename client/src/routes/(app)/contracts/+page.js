export const prerender = true;

export async function load({ params }) {
    let response = await fetch("http://localhost:8000/api/v1/weddings/");
    let contracts = await response.json();
    return {
        contracts: contracts
    };
}