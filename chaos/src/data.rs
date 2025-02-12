use axum::{http::StatusCode, response::IntoResponse, Json};
use serde::{Deserialize, Serialize};

pub async fn process_data(Json(request): Json<DataRequest>) -> impl IntoResponse {
    // Calculate sums and return response

    let mut string_len:i64 = 0;
    let mut int_sum = 0;

    for data_entry in request.data {
        match data_entry {
            Data::Str(str) => string_len+=str.len() as i64,
            Data::Num(num) => int_sum+=num,
        }
    }

    let response = DataResponse {
        string_len,
        int_sum
    };

    (StatusCode::OK, Json(response))
}

#[derive(Deserialize)]
pub struct DataRequest {
    // Add any fields here
    pub data: Vec<Data>
}

#[derive(Deserialize)]
#[serde(untagged)]
pub enum Data {
    Str(String),
    Num(i64)
}

#[derive(Serialize)]
pub struct DataResponse {
    // Add any fields here
    pub string_len: i64,
    pub int_sum: i64
}
