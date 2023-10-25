import Link from 'next/link';

export default function Home() {
  return (
    <div className="container h-full">
      <Link href={'/flowmap'}>go to flowmap~</Link>
    </div>
  );
}
