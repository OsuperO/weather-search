import React, { useState, useEffect } from 'react';
import { Button, Input, Stack, Box } from '@mui/joy';
import SearchIcon from '@mui/icons-material/Search';
import axois from 'axios';


function App() {
  const [weatherData, setWeatherData] = useState("");
  const [city, setCity] = useState("");
  const [Loading, setLoading] = useState(false);
  
  const fetchWeatherData = async () => {
    if (!city) {
      return;
    }
    // 使用axios发送请求
    const data = {
      city: city
    };
    const responseData1 = {
        "data": {
          "current": {
            "cloudcover": 0,
            "feelslike": 26,
            "humidity": 74,
            "is_day": "yes",
            "observation_time": "08:42 AM",
            "precip": 0.5,
            "pressure": 1015,
            "temperature": 24,
            "uv_index": 0,
            "visibility": 10,
            "weather_code": 113,
            "weather_descriptions": [
              "Sunny"
            ],
            "weather_icons": [
              "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
            ],
            "wind_degree": 340,
            "wind_dir": "NNW",
            "wind_speed": 11
          },
          "location": {
            "country": "China",
            "lat": "31.005",
            "localtime": "2024-10-14 16:42",
            "localtime_epoch": 1728924120,
            "lon": "121.409",
            "name": "Shanghai",
            "region": "Shanghai",
            "timezone_id": "Asia/Shanghai",
            "utc_offset": "8.0"
          },
          "request": {
            "language": "en",
            "query": "Shanghai, China",
            "type": "City",
            "unit": "m"
          }
        },
        "msg": "success"
      }
      // setWeatherData(responseData);
      // console.log(responseData);
    setLoading(true);
    const responseData = await axois.post("https://127.0.0.1:8443/weather", data).then(res => {
        console.log(res.data);
        return res.data;
      })
    setWeatherData(responseData);
  }


  return (
    <Box>
      <Stack 
      spacing={2}
      direction="column"
      sx={{
        marginTop: "2vh",
        justifyContent: "center",
        alignItems: "center",
      }}>
        <Input
          placeholder="请输入城市名称"
          onChange={(e) => setCity(e.target.value)}
          endDecorator={
            <Button 
            variant="soft" 
            color="neutral" 
            startDecorator={<SearchIcon />}
            onClick={fetchWeatherData}
            >
              查询
            </Button>
          }
          sx={{ width: 300 }}
        />
        {/* <Box>{weatherData}</Box> */}
        <Box
          sx={{
            width: 600,
            height: 300,
            // 半透明背景色
            backgroundColor: "rgba(0, 0, 0, 0.3)",
            borderRadius: "20px",  // 圆角
            padding: "10px",
          }}
        >
          {
            weatherData ?
            <Stack 
            spacing={2}
            sx={{
            marginTop: "1vh",
            justifyContent: "center",
            alignItems: "center",
            }}>         
              <Box>{weatherData.data.location.country} {weatherData.data.location.region} {weatherData.data.location.name}</Box>
              <Stack direction="row" spacing={2}>
                <Box>{city}</Box>
                <Box>{city}</Box>
                <Box>{city}</Box>
              </Stack>
            </Stack>
            : Loading ?
            <Box>Loading...</Box>
            :
            <Box>请输入城市名称查询</Box>
            
          }
          
          {/* {JSON.stringify(weatherData)} */}
        </Box>
      </Stack>
    </Box>

  );
};
export default App;
