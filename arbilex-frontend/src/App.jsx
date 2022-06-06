import React, { useState, useEffect } from 'react';
import image from './assets/img.jpeg';
import apiClient from './Interfaces/Http';
import './App.css';
import SCSlider from './Components/SCSlider';
import dateFormatter from './Helpers/DateFormatter';

function App() {
  const startDate = new Date(1791, 7, 2); // The date of the first argument before SCOTUS
  const [sliderValue, setSliderValue] = useState('##/##/####');
  const [justiceTerm, setJusticeTerm] = useState('####');
  const [decisionDuration, setDecisionDuration] = useState('####');
  const [disentingJustice, setDisentingJustice] = useState('####');

  const fetchData = async (days) => {
    const res = await apiClient.get(`/?d=${days}`);
    return res;
  };

  const updateData = (days) => {
    fetchData(days).then((res) => {
      setJusticeTerm(res.data.term_duration);
      setDecisionDuration(res.data.decision_duration);
      setDisentingJustice(res.data.disenting_justice);
    });
  };

  useEffect(() => updateData(60000), []);

  const updater = (args) => {
    setSliderValue(dateFormatter(startDate, args[0]));
  };

  const changer = (args) => {
    updateData(args[0]);
  };

  return (
    <div className="container">
      <h1>Design</h1>
      <div className="panel large">
        <div className="panel-content">
          <img alt="SCOTUS" src={image} />
          <div>
            <h1 className="headline">Lorem ipsum dolor sit amet consectetur</h1>
            <div className="head-content">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis vel eros donec ac odio tempor orci dapibus ultrices. Ornare lectus sit amet est placerat in egestas erat imperdiet. Etiam erat velit scelerisque in dictum non consectetur a. Massa sed elementum tempus egestas. Quis
            </div>
            <br />
            <br />
            <br />
            <input className="blue-button" type="button" value="This is a button" />
          </div>
        </div>
      </div>
      <h1>Data</h1>
      <div className="row">
        <div className="panel small">
          <div className="panel-content">
            <h2>{justiceTerm}</h2>
            <div className="panel-caption">Justice Term Duration</div>
            <div className="panel-subcaption">Average Duration (years)</div>
          </div>
        </div>
        <div className="panel small middle">
          <div className="panel-content">
            <h2>{decisionDuration}</h2>
            <div className="panel-caption">Decision Duration</div>
            <div className="panel-subcaption">Average Duration (days)</div>
          </div>
        </div>
        <div className="panel small">
          <div className="panel-content">
            <h2>{disentingJustice}</h2>
            <div className="panel-caption-container">
              <div className="panel-caption">Most Disenting Justice</div>
              <div className="panel-subcaption">Name</div>
            </div>
          </div>
        </div>
        <div className="panel medium no-border">
          <div className="panel-content no-border">
            <div className="slider-caption">Filter to justices appointed after:</div>
            <div className="slider-caption">
              {sliderValue}
              {' '}
            </div>
            <br />
            <br />
            <div className="slider-container"><SCSlider update={updater} change={changer} /></div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
