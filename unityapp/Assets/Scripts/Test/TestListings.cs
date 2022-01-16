using System;
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.Replay;
using UnityEngine.Networking;

namespace Unity.Metacast.Demo
{
    /// <summary>
    ///     Populate UIBrowser with test json data
    /// </summary>
    public class TestListings : MonoBehaviour
    {
        [SerializeField] private TextAsset m_TestJson;

        /// <summary>
        ///     Start is called on the frame when a script is enabled just
        ///     before any of the Update methods are called the first time.
        /// </summary>
        private async void Start()
        {
            //TODO Instead of a TextAsset pass JSON result from the web server.
            var url = "http://localhost:8000/api/games/";
            using var www = UnityWebRequest.Get(url);
            www.SetRequestHeader("Content-Type", "application/json");
            var operation = www.SendWebRequest();

            while(!operation.isDone)
                await Task.Yield();
            
            
            if (www.result == UnityWebRequest.Result.Success){
                Debug.Log($"Success :{www.downloadHandler.text}");
                UIBrowser.instance.Init(www.downloadHandler.text);
            }
            else
                Debug.Log($"Failed :{www.error}");
        }
    }
}
