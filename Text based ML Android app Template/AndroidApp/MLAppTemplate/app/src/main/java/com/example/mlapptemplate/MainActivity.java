package com.example.mlapptemplate;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import com.example.mlapptemplate.ApiHandler.ApiController;

import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    // log Tag
    private final String TAG = "ApiController";

    // Api Controller Object
    private final ApiController apiController = new ApiController();

    // Buttons
    private Button connectBtn, predictBtn;

    // input text buttons
    private EditText urlData, inputData;

    // Response Text View
    private TextView response;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // buttons created
        connectBtn = findViewById(R.id.connectBtn);
        predictBtn = findViewById(R.id.predictBtn);


        // Connect to API Method
        connectBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                urlData = findViewById(R.id.urlEditText);
                String url = urlData.getText().toString();
                Log.d("ApiController", "onClick: " + url);
                if (!url.isEmpty())
                    apiController.createSession(url);
            }
        });

        // Predictor
        predictBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                inputData = findViewById(R.id.inputEditText);

                Log.d(TAG, "onClick: Post Btn");

                // response view button
                response = findViewById(R.id.responseView);
                if (!inputData.getText().toString().isEmpty()) {
                    try {
                        apiController.webHookHandler(inputData.getText().toString(), response);
                    } catch (IOException e) {
                        e.printStackTrace();
                        Log.e(TAG, "onClick: ", e);
                    }
                }
            }
        });


    }
}
