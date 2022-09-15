export const groupByStudent = (array) => {
  const obj = {};

  array.forEach((el) => {
    if (!obj[el.students_name]) {
      obj[el.students_name] = [];
    }

    obj[el.students_name].push(el);
  });

  const result = [];

  for (let arr of Object.values(obj)) {
    result.push(...groupBySubject(arr));
  }

  return result;
};

export const groupBySubject = (array) => {
  const obj = {};

  array.forEach((el) => {
    if (!obj[el.lessons_name]) {
      obj[el.lessons_name] = [];
    }

    obj[el.lessons_name].push(el);
  });

  const result = [];

  for (let arr of Object.values(obj)) {
    result.push({
      ...arr[0],
      mark: undefined,
      marks: arr.map((el) => el.mark),
    });
  }

  return result;
};
