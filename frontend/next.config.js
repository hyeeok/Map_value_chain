/** @type {import('next').NextConfig} */
const nextConfig = {
  async redirects() {
    return [
      {
        source: '/',
        destination: '/flowmap',
        permanent: true,
      },
    ];
  },
};

module.exports = nextConfig;
