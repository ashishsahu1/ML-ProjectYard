package com.example.mlapptemplate.ApiHandler;

import android.util.Log;
import android.widget.TextView;
import com.google.gson.JsonObject;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

import java.io.IOException;

public class ApiController {

    private final String TAG = "ApiController";
    private String url;
    private ApiServiceProvider apiServiceProvider;


    public void createSession(String inputUrl) {
        Log.d(TAG, "createSession: Session is being created");
        url = inputUrl;
        connect();
    }

    private void connect() {
        Retrofit retrofit = new Retrofit.Builder().baseUrl(url)
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        try {
            apiServiceProvider = retrofit.create(ApiServiceProvider.class);
            Log.d(TAG, "connect: connected ");
        } catch (Exception e) {
            Log.e(TAG, "error while creating a session :", e);
        }
    }

    public void webHookHandler(String inputData, TextView responseBtn) throws IOException {
        Log.d(TAG, "webHookHandler: Input Data for prediction = " + inputData);
        JsonObject jsonObject = new JsonObject();
        jsonObject.addProperty("data", inputData);
        Log.d(TAG, "webHookHandler: Data callRequest = "+jsonObject);
        Call<ResponseBody> ab = apiServiceProvider.sendDataToWebHook(jsonObject);
        ab.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                if (response.isSuccessful()) {
                    try {
                        if (response.body() != null) {
                            ResponseBody result = response.body();
                            responseBtn.setText(result.string());
                            Log.d(TAG, "onResponse: Response from the APi "+result.toString());
                        }else{
                            Log.d(TAG, "onResponse: Null returned from API");
                        }
                    } catch (Exception e) {
                        Log.d(TAG, "onResponse: error while getting the response data ", e);
                    }
                }else{
                    Log.d(TAG, "onResponse: no response from the API");
                }
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                Log.e(TAG, "onFailure: ", t);
            }
        });
    }


}
