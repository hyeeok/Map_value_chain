export const formatDate = (inputDate: string | null) => {
  if (!inputDate) {
    return inputDate;
  }
  const year = inputDate.slice(0, 4);
  const month = parseInt(inputDate.slice(4, 6), 10);
  const day = parseInt(inputDate.slice(6), 10);
  const formattedDate = `${year}년 ${month}월 ${day}일`;
  return formattedDate;
};

export const formatListDate = (inputDate: string | null) => {
  if (!inputDate) {
    return inputDate;
  }
  const parts = inputDate.split('/');
  const year =
    parseInt(parts[0]) < 23
      ? 2000 + parseInt(parts[0])
      : 1900 + parseInt(parts[0]);
  const month = parseInt(parts[1]);
  const day = parseInt(parts[2]);
  const formattedDate = `${year}년 ${month}월 ${day}일`;
  return formattedDate;
};
