package com.example.mlapptemplate.ApiHandler;

import android.content.Context;
import android.util.Log;
import com.google.gson.JsonObject;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ApiController {

    private final String TAG = "ApiController";
    private String url;
    private ApiServiceProvider apiServiceProvider;
    private Context context;
    private List<String> res = new ArrayList<>();

    public List<String> getRes() {
        return res;
    }


    public void createSession(String inputUrl) {
        url = inputUrl;
        connect();
    }

    private void connect()
    {
        Retrofit retrofit = new Retrofit.Builder().baseUrl(url)
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        try {
            apiServiceProvider = retrofit.create(ApiServiceProvider.class);
            Log.d(TAG, "connect: connected ");
        } catch (Exception e) {
            Log.e(TAG, "error :", e);
        }
    }

    public void webHookHandler(String inputData) {
        Log.d(TAG, "webHookHandler: "+inputData);
        JsonObject jsonObject = new JsonObject();
        jsonObject.addProperty("data", inputData);
        Call<ResponseBody> ab = apiServiceProvider.sendDataToWebHook(jsonObject);
        ab.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                if (response.isSuccessful()) {
                    try {
                        if (response.body() != null) {
                            res.add(response.body().string());
                            Log.d(TAG, "onResponse: "+ res.get(0));
                        }
                    } catch (Exception e) {
                        Log.d(TAG, "onResponse: error while getting the response data /n", e);
                    }
                }
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                Log.e(TAG, "onFailure: ",t );
            }
        });
        Log.d(TAG, "webHookHandler: 11");
    }


}
