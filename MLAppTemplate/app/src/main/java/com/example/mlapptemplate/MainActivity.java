package com.example.mlapptemplate;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import com.example.mlapptemplate.ApiHandler.ApiController;

public class MainActivity extends AppCompatActivity {

    private final String TAG = "ApiController";

    private ApiController apiController = new ApiController();

    private Button connectBtn,predictBtn;
    private EditText urlData,inputData;
    private TextView response;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // buttons
        connectBtn = findViewById(R.id.connectBtn);
        predictBtn = findViewById(R.id.predictBtn);


        connectBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                urlData = findViewById(R.id.urlEditText);
                String url = urlData.getText().toString();
                Log.d("ApiController", "onClick: "+url);
                if (!url.isEmpty())
                apiController.createSession(url);
            }
        });

        predictBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                inputData = findViewById(R.id.inputEditText);

                response = findViewById(R.id.responseView);
                if (!inputData.getText().toString().isEmpty())
                {

                    apiController.webHookHandler(inputData.getText().toString());
//                    Log.d(TAG, "onClick: "+apiController.getRes().get(0));
                    response.setText("r");
                }
            }
        });

    }
}
