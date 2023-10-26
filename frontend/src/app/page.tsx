import Link from 'next/link';

export default function Home() {
  return (
    <div className="container">
      <Link href={'/flowmap'}>go to flowmap~</Link>
    </div>
  );
}
