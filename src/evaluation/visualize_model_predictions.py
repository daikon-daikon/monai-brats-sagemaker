model.load_state_dict(
    torch.load(os.path.join(root_dir, "best_metric_model.pth"))
)
model.eval()
with torch.no_grad():
    # select one image to evaluate and visualize the model output
    val_input = val_ds[6]["image"].unsqueeze(0).to(device)
    roi_size = (128, 128, 64)
    sw_batch_size = 4
    val_output = inference(val_input)
    val_output = post_trans(val_output[0])
    plt.figure("image", (24, 6))
    for i in range(4):
        plt.subplot(1, 4, i + 1)
        plt.title(f"image channel {i}")
        plt.imshow(val_ds[6]["image"][i, :, :, 70].detach().cpu(), cmap="gray")
    #save for TrainingJob
    plt.savefig(
    "/opt/ml/model/image_channel.png",
    bbox_inches="tight",
    dpi=300,
    facecolor="white"
    )
    plt.show()
    #visualize the 3 channels label corresponding to this image
    plt.figure("label", (18, 6))
    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.title(f"label channel {i}")
        plt.imshow(val_ds[6]["label"][i, :, :, 70].detach().cpu())
    #save for TrainingJob
    plt.savefig(
    "/opt/ml/model/label_channel.png",
    bbox_inches="tight",
    dpi=300,
    facecolor="white"
    )
    plt.show()
    
    # visualize the 3 channels model output corresponding to this image
    plt.figure("output", (18, 6))
    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.title(f"output channel {i}")
        plt.imshow(val_output[i, :, :, 70].detach().cpu())
    #save for TrainingJob
    plt.savefig(
    "/opt/ml/model/output_channel.png",
    bbox_inches="tight",
    dpi=300,
    facecolor="white"
    )
    plt.show()
