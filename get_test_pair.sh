nohup python ./src/cal_id_scene.py \
      --feature-root-folder=/workspace/data/face-idcard-1M/face-idcard-1M-mtcnn-aligned-112x112/idcard_vs_scene_7570/feature/model-r100-spa-m2.0-4gpu-blueface_ansia_95660_and_deepint_ansia_143050_more_iter-ep216 \
      --gallery-list-path=/workspace/data/face-idcard-1M/face-idcard-1M-mtcnn-aligned-112x112/idcard_vs_scene_7570/feature/model-r100-spa-m2.0-4gpu-blueface_ansia_95660_and_deepint_ansia_143050_more_iter-ep216/gallery.lst \
      --probe-list-path=/workspace/data/face-idcard-1M/face-idcard-1M-mtcnn-aligned-112x112/idcard_vs_scene_7570/feature/model-r100-spa-m2.0-4gpu-blueface_ansia_95660_and_deepint_ansia_143050_more_iter-ep216/probe.lst \
      --score-save-path=./id_scene.txt > ./nohup.log 2>&1 & 
    
