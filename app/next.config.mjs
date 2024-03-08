/** @type {import('next').NextConfig} */
const nextConfig = {
  rewrites: async () => [
    {
      source: "/cocktail", // Matches requests to /api/cocktail
      destination: "http://127.0.0.1:8000/cocktail", // Forward to backend URL
    },
  ],
};

export default nextConfig;
