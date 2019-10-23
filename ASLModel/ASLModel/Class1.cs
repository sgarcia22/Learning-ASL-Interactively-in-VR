using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Windows.AI.MachineLearning;
using System.Threading.Tasks;

namespace ASLModel
{
    public static class Model
    {

        private LearningModel m_model = null;
        private LearningModelSession m_session;
        private LearningModelDeviceKind m_inferenceDeviceSelected = LearningModelDeviceKind.Default;
        private LearningModelBinding m_binding;

        /// Load in the model
        private async Task LoadModelAsync(string fileName, bool gpu)
        {
            StorageFile modelFile = await StorageFile.GetFileFromApplicationUriAsync(new Uri($"ms-appx:///Assets/{fileName}"));
            m_model =  await LearningModel.LoadFromStorageFileAsync(modelFile);
            m_inferenceDeviceSelected = gpu ? LearningModelDeviceKind.DirectXHighPerformance : LearningModelDeviceKind.Cpu;
            m_session = new LearningModelSession(m_model, new LearningModelDevice(m_inferenceDeviceSelected));
        }

        /// Evaluate the input with the model
        private async Task EvaluateHandSign(float [] inputValues)
        {
            try {
                m_binding = new LearningModelBinding(session);
                string out_name;
                //TODO
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex.ToString());
            }
        }
    }
}
