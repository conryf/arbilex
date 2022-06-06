const dateFormatter = (startDate, days) => {
  const dt = new Date(startDate.getTime());
  dt.setDate(startDate.getDate() + days);
  return `${dt.getMonth() + 1}/${dt.getDate()}/${dt.getFullYear()}`;
};

export default dateFormatter;
