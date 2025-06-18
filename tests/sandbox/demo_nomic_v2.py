from sentence_transformers import SentenceTransformer
import time

print("🚀 Đang tải model nomic-ai/nomic-embed-text-v2-moe...")
start_time = time.time()

model = SentenceTransformer("nomic-ai/nomic-embed-text-v2-moe", trust_remote_code=True)

load_time = time.time() - start_time
print(f"✅ Model đã được tải thành công! Thời gian: {load_time:.2f}s")

sentences = ["Hello!", "¡Hola!", "Xin chào!"]
print(f"📝 Các câu để embedding: {sentences}")

print("🔄 Đang sinh embedding...")
embed_start = time.time()

embeddings = model.encode(sentences, prompt_name="passage")

embed_time = time.time() - embed_start
print(f"✅ Hoàn thành embedding! Thời gian: {embed_time:.2f}s")

print(f"📊 Kết quả:")
print(f"   - Số câu: {len(sentences)}")
print(f"   - Kích thước embedding: {embeddings.shape}")
print(f"   - Kiểu dữ liệu: {embeddings.dtype}")
print(f"   - Embedding đầu tiên (5 giá trị): {embeddings[0][:5]}")

print("🎉 Test thành công!")
