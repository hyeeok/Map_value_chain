/** @type {import('next').NextConfig} */
const nextConfig = {
  async redirects() {
    return [
      {
        source: '/',
        destination: '/value-chain',
        permanent: true,
      },
    ];
  },
};

module.exports = nextConfig;
