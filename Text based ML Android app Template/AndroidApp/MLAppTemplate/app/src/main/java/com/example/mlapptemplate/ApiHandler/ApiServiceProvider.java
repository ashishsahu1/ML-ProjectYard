package com.example.mlapptemplate.ApiHandler;

import com.google.gson.JsonObject;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface ApiServiceProvider {

    @POST("webhook")
    Call<ResponseBody> sendDataToWebHook(@Body JsonObject jsonObject);

}
