const initialNodes = [
  {
    id: '1',
    position: { x: 0, y: 0 },
    data: { label: '농림축수산' },
    type: 'custom',
  },
  {
    id: '2',
    position: { x: 200, y: 0 },
    data: { label: '의학/헬스케어' },
    type: 'custom',
  },
  {
    id: '3',
    position: { x: 0, y: 200 },
    data: { label: '금융/부동산' },
    type: 'custom',
  },
  {
    id: '4',
    position: { x: 200, y: 200 },
    data: { label: '에너지/자원' },
    type: 'custom',
  },
  {
    id: '5',
    position: { x: 200, y: 500 },
    data: { label: '소재/기초제품' },
    type: 'custom',
  },
];

const initialEdges = [
  {
    id: '1-2',
    source: '1',
    sourceHandle: 'right',
    target: '2',
    targetHandle: 'left',
  },
  {
    id: '1-4',
    source: '1',
    sourceHandle: 'bottom',
    target: '4',
    targetHandle: 'top',
  },
];

const mvc = [
  {
    category: '농림축수산',
    color: 1,
    domains: [{ label: '농축산업' }, { label: '수산업' }, { label: '임업' }],
    themes: [{ label: '스마트팜' }],
  },
  {
    category: '의학/헬스케어',
    color: 2,
    domains: [
      { label: '반려동물/수의학' },
      { label: '바이오/생물공학' },
      { label: '제약/의약품' },
      { label: '의료기기/용품' },
      { label: '헬스케어 기술/서비스' },
      { label: '의료기관 및 서비스' },
    ],
    themes: [
      { label: '백신/방역/진단시약' },
      { label: '실버산업/시니어' },
      { label: '건강 기능식품' },
      { label: '메디컬뷰피/더마코스메틱' },
      { label: '원격진료' },
    ],
  },
  {
    category: '금융/부동산',
    color: 1,
    domains: [
      { label: '은행' },
      { label: '보험' },
      { label: '부동산/리스' },
      { label: '금융서비스' },
    ],
    themes: [{ label: '인터넷/은행' }, { label: '핀테크/전자결제' }],
  },
  {
    category: '에너지/자원',
    color: 3,
    domains: [
      { label: '폐기물/재생/광업지원' },
      { label: '에너지장비/서비스' },
      { label: '석유/가스/석탄' },
      { label: '신재생 에너지' },
    ],
    themes: [
      { label: '원자력' },
      { label: '탄소중립/자원순환' },
      { label: '수소' },
    ],
  },
  {
    category: '소재/기초제품',
    color: 4,
    domains: [
      { label: '비금속 채광/제조' },
      { label: '종이/목재제품' },
      { label: '용기/포장지' },
      { label: '금속 채광/제조' },
      { label: '화학제조' },
      { label: '고무/플라스틱' },
    ],
    themes: [{ label: '신소재/카본/나노' }],
  },
];

export { initialEdges, initialNodes, mvc };
