import React, { useState, useEffect } from 'react';
import { csv } from 'd3';

const csvUrl =
  'https://gist.githubusercontent.com/Debiday/5e789cf011f020169e6d17dc7ec7404d/raw/8e3d60b02c20c41482d57c6764910927f07239a8/CA.csv';

export const useData = () => {
  const [data, setData] = useState(null);

    useEffect(() => {
    const row = d => {
      d.case= +d.case;
      d.date_missing = new Date(d.date_missing);
      d.lname = d.lname;
    	d.fname = d.fname;
      d.age = +d.age;
      d.city = d.city;
      d.county = d.county;
      d.state= d.state;
      d.gender = d.gender;
      d.ethnicity = d.ethnicity;
      return d;
    };
    csv(csvUrl, row).then(setData);
  }, []);
  
  return data;
};