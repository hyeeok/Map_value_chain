import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <Link href={'/flowmap'}>go to flowmap</Link>
    </div>
  );
}
